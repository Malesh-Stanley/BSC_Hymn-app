from __future__ import annotations

import asyncio

import flet as ft

from .hymns import HYMNS, Hymn

_THEME_BY_NAME = {
    "system": ft.ThemeMode.SYSTEM,
    "light": ft.ThemeMode.LIGHT,
    "dark": ft.ThemeMode.DARK,
}

_ROUTES_WITH_NAV = {
    "/home": 0,
    "/favorites": 1,
    "/settings": 2,
}


class HymnApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.search_query = ""
        self.favorite_ids: set[int] = set()
        self.theme_name = "system"
        self.font_size = 16.0
        self._splash_started = False
        self._splash_progress_value = 0.0
        self._splash_progress_control: ft.ProgressBar | None = None

    def setup(self) -> None:
        self.page.title = "BSC Song Book"
        self.page.padding = 0
        self.page.theme_mode = _THEME_BY_NAME[self.theme_name]

        self._load_state()

        self.page.on_route_change = self._handle_route_change
        self.page.go(self.page.route or "/")

    def _load_state(self) -> None:
        if hasattr(self.page, "client_storage"):
            self._load_state_from_client_storage()
            return

        if hasattr(self.page, "shared_preferences"):
            self.page.run_task(self._load_state_from_shared_preferences)

    def _load_state_from_client_storage(self) -> None:
        stored_favorites = self.page.client_storage.get("hymn.favorite_ids")
        if isinstance(stored_favorites, list):
            parsed_ids: set[int] = set()
            for item in stored_favorites:
                try:
                    parsed_ids.add(int(item))
                except (TypeError, ValueError):
                    continue
            self.favorite_ids = parsed_ids

        stored_theme = self.page.client_storage.get("hymn.theme_name")
        if isinstance(stored_theme, str) and stored_theme in _THEME_BY_NAME:
            self.theme_name = stored_theme
            self.page.theme_mode = _THEME_BY_NAME[self.theme_name]

        stored_font_size = self.page.client_storage.get("hymn.font_size")
        if isinstance(stored_font_size, (int, float)) and 14 <= float(stored_font_size) <= 30:
            self.font_size = float(stored_font_size)

    async def _load_state_from_shared_preferences(self) -> None:
        prefs = self.page.shared_preferences

        stored_favorites = await prefs.get("hymn.favorite_ids")
        if isinstance(stored_favorites, list):
            parsed_ids: set[int] = set()
            for item in stored_favorites:
                try:
                    parsed_ids.add(int(item))
                except (TypeError, ValueError):
                    continue
            self.favorite_ids = parsed_ids

        stored_theme = await prefs.get("hymn.theme_name")
        if isinstance(stored_theme, str) and stored_theme in _THEME_BY_NAME:
            self.theme_name = stored_theme
            self.page.theme_mode = _THEME_BY_NAME[self.theme_name]

        stored_font_size = await prefs.get("hymn.font_size")
        if isinstance(stored_font_size, (int, float)) and 14 <= float(stored_font_size) <= 30:
            self.font_size = float(stored_font_size)

        self._render_current_route()

    def _save_favorites(self) -> None:
        values = sorted(self.favorite_ids)
        if hasattr(self.page, "client_storage"):
            self.page.client_storage.set("hymn.favorite_ids", values)
            return

        if hasattr(self.page, "shared_preferences"):
            self.page.run_task(
                self._save_to_shared_preferences,
                "hymn.favorite_ids",
                [str(item) for item in values],
            )

    def _save_theme(self) -> None:
        if hasattr(self.page, "client_storage"):
            self.page.client_storage.set("hymn.theme_name", self.theme_name)
            return

        if hasattr(self.page, "shared_preferences"):
            self.page.run_task(self._save_to_shared_preferences, "hymn.theme_name", self.theme_name)

    def _save_font_size(self) -> None:
        if hasattr(self.page, "client_storage"):
            self.page.client_storage.set("hymn.font_size", self.font_size)
            return

        if hasattr(self.page, "shared_preferences"):
            self.page.run_task(self._save_to_shared_preferences, "hymn.font_size", self.font_size)

    async def _save_to_shared_preferences(self, key: str, value: str | int | float | bool | list[str]) -> None:
        await self.page.shared_preferences.set(key, value)

    def _handle_route_change(self, _: ft.RouteChangeEvent) -> None:
        self._render_current_route()

    def _render_current_route(self) -> None:
        route = self.page.route or "/"
        self.page.clean()

        if route == "/":
            self.page.add(self._build_splash_page())
            return

        content = self._build_route_content(route)
        self.page.add(
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        ft.Container(expand=True, padding=8, content=content),
                        self._build_bottom_navigation(route),
                    ],
                ),
            )
        )

    def _build_route_content(self, route: str) -> ft.Control:
        if route == "/home":
            return self._build_home_page()
        if route == "/favorites":
            return self._build_favorites_page()
        if route == "/settings":
            return self._build_settings_page()
        if route.startswith("/hymn/"):
            hymn = self._hymn_from_route(route)
            if hymn is not None:
                return self._build_hymn_page(hymn)

        return ft.Column(
            controls=[
                ft.Text("Page not found", size=24, weight=ft.FontWeight.W_700),
                ft.TextButton("Go to Home", on_click=lambda _: self.page.go("/home")),
            ]
        )

    def _build_splash_page(self) -> ft.Control:
        if not self._splash_started:
            self._splash_started = True
            self.page.run_task(self._auto_leave_splash)

        return ft.SafeArea(
            expand=True,
            content=ft.Container(
                expand=True,
                padding=32,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=[ft.Colors.AMBER_100, ft.Colors.ORANGE_200, ft.Colors.RED_200],
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.LIBRARY_MUSIC, size=72, color=ft.Colors.BROWN_800),
                        ft.Text(
                            " BSC HymnBook",
                            size=40,
                            weight=ft.FontWeight.W_700,
                            color=ft.Colors.BROWN_900,
                        ),
                        ft.Text(
                            "BSC songs for worship and practice",
                            size=16,
                            color=ft.Colors.BROWN_700,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        # Thick linear progress bar that fills during the splash duration
                        ft.Container(
                            width=360,
                            content=ft.ProgressBar(
                                value=self._splash_progress_value,
                                height=8,
                            ),
                        ),
                        ft.TextButton(
                            content=ft.Text(
                                "Get Started",
                                weight=ft.FontWeight.W_700,
                                color=ft.Colors.BLACK,
                            ),
                            key="enter_from_splash",
                            style=ft.ButtonStyle(color=ft.Colors.BLACK),
                            on_click=lambda _: self.page.go("/home"),
                        ),
                    ],
                ),
            ),
        )

    async def _auto_leave_splash(self) -> None:
        # Animate the linear progress bar over 5 seconds, then continue to home.
        duration = 5.0
        steps = 50
        delay = duration / steps
        # Reset progress
        self._splash_progress_value = 0.0

        for i in range(steps):
            self._splash_progress_value = min(1.0, self._splash_progress_value + 1.0 / steps)
            # update any existing progress control in the UI
            try:
                # find the control by key: ProgressBar may not have a stable ref, so update via page.update
                # Re-rendering the route will recreate controls; here we set page.update to refresh value binding
                self.page.update()
            except Exception:
                pass
            await asyncio.sleep(delay)

        self._splash_progress_value = 1.0
        try:
            self.page.update()
        except Exception:
            pass

        if self.page.route == "/":
            self.page.go("/home")

    def _build_home_page(self) -> ft.Control:
        hymns = self._filtered_hymns()

        hymn_tiles = [self._build_hymn_tile(hymn) for hymn in hymns]
        if not hymn_tiles:
            hymn_tiles = [
                ft.Container(
                    key="home_no_results",
                    padding=20,
                    content=ft.Text("No hymns matched your search."),
                )
            ]

        return ft.Column(
            expand=True,
            spacing=12,
            controls=[
                ft.Text("Hymns", size=28, weight=ft.FontWeight.W_700),
                ft.TextField(
                    key="search_field",
                    value=self.search_query,
                    label="Search hymn title or number",
                    prefix_icon=ft.Icons.SEARCH,
                    on_change=self._on_search_change,
                ),
                ft.Text(f"{len(hymns)} song(s)", size=12, color=ft.Colors.GREY_700),
                ft.ListView(expand=True, spacing=8, controls=hymn_tiles),
            ],
        )

    def _build_favorites_page(self) -> ft.Control:
        favorite_hymns = [h for h in HYMNS if h.id in self.favorite_ids]

        if not favorite_hymns:
            return ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.Icons.FAVORITE_BORDER, size=64),
                    ft.Text("No favourites yet", size=22, key="empty_favorites"),
                    ft.Text("Tap the heart icon on a hymn to save it."),
                ],
            )

        return ft.Column(
            expand=True,
            spacing=12,
            controls=[
                ft.Text("Favourites", size=28, weight=ft.FontWeight.W_700),
                ft.ListView(
                    expand=True,
                    spacing=8,
                    controls=[self._build_hymn_tile(hymn) for hymn in favorite_hymns],
                ),
            ],
        )

    def _build_settings_page(self) -> ft.Control:
        return ft.Column(
            expand=True,
            spacing=16,
            controls=[
                ft.Text("Settings", size=28, weight=ft.FontWeight.W_700),
                ft.Dropdown(
                    key="theme_dropdown",
                    label="Theme",
                    value=self.theme_name,
                    options=[
                        ft.dropdown.Option("system", "System"),
                        ft.dropdown.Option("light", "Light"),
                        ft.dropdown.Option("dark", "Dark"),
                    ],
                    on_select=self._on_theme_change,
                ),
                ft.Column(
                    controls=[
                        ft.Text(f"Font size: {int(self.font_size)}", key="font_size_value"),
                        ft.Slider(
                            key="font_size_slider",
                            min=14,
                            max=30,
                            divisions=8,
                            value=self.font_size,
                            label="{value}",
                            on_change=self._on_font_size_change,
                        ),
                    ]
                ),
                ft.Divider(),
                ft.Text("About Us", size=22, weight=ft.FontWeight.W_600),
                ft.Text(
                    "Bright Star Choir HymnBook. \n" 
                    "Fully offline, suitable for practice and worship sessions. \n"
                    "Browse, search and save your favourite hymns anytime. \n"
                    "Developed by: JM STANLEY.",
                ),
            ],
        )

    def _build_hymn_page(self, hymn: Hymn) -> ft.Control:
        is_favorite = hymn.id in self.favorite_ids

        return ft.Column(
            expand=True,
            spacing=12,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.TextButton(
                            "Back",
                            key="hymn_back",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda _: self.page.go("/home"),
                        ),
                        ft.IconButton(
                            key="hymn_detail_fav_toggle",
                            icon=ft.Icons.FAVORITE if is_favorite else ft.Icons.FAVORITE_BORDER,
                            icon_color=ft.Colors.RED if is_favorite else ft.Colors.GREY_400,
                            on_click=lambda _: self._toggle_favorite_and_refresh(hymn.id),
                        ),
                    ],
                ),
                ft.Text(
                    hymn.title,
                    size=self.font_size + 10,
                    weight=ft.FontWeight.W_700,
                ),
                ft.ListView(
                    expand=True,
                    spacing=10,
                    controls=[
                        ft.Container(
                            padding=12,
                            border_radius=10,
                            bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.BLUE_GREY),
                            content=ft.Text(
                                verse.replace(" / ", "\n").replace("/", "\n"),
                                size=self.font_size,
                            ),
                        )
                        for verse in hymn.verses
                    ],
                ),
            ],
        )

    def _build_hymn_tile(self, hymn: Hymn) -> ft.Control:
        is_favorite = hymn.id in self.favorite_ids

        return ft.Container(
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.BLUE_GREY),
            border_radius=12,
            padding=4,
            content=ft.ListTile(
                key=f"hymn_tile_{hymn.id}",
                title=ft.Row(
                    spacing=12,
                    controls=[
                        ft.Text(str(getattr(hymn, "number", hymn.id)), size=14, weight=ft.FontWeight.W_700),
                        ft.Text(hymn.title, size=max(14, self.font_size - 1), weight=ft.FontWeight.W_600),
                    ],
                ),
                trailing=ft.IconButton(
                    key=f"fav_toggle_{hymn.id}",
                    icon=ft.Icons.FAVORITE if is_favorite else ft.Icons.FAVORITE_BORDER,
                    icon_color=ft.Colors.RED if is_favorite else ft.Colors.GREY_400,
                    on_click=lambda _: self._toggle_favorite_and_refresh(hymn.id),
                ),
                on_click=lambda _: self.page.go(f"/hymn/{hymn.id}"),
            ),
        )

    def _build_bottom_navigation(self, route: str) -> ft.Control:
        selected_index = _ROUTES_WITH_NAV.get(route, 0)

        return ft.NavigationBar(
            key="bottom_nav",
            selected_index=selected_index,
            on_change=self._on_nav_change,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FAVORITE_BORDER,
                    selected_icon=ft.Icons.FAVORITE,
                    label="Favourites",
                ),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS_OUTLINED, selected_icon=ft.Icons.SETTINGS, label="Settings"),
            ],
        )

    def _hymn_from_route(self, route: str) -> Hymn | None:
        try:
            hymn_id = int(route.rsplit("/", 1)[1])
        except (IndexError, ValueError):
            return None

        for hymn in HYMNS:
            if hymn.id == hymn_id:
                return hymn
        return None

    def _filtered_hymns(self) -> list[Hymn]:
        query = self.search_query.strip().lower()
        if not query:
            return HYMNS

        def matches(hymn: Hymn) -> bool:
            if query in hymn.title.lower():
                return True

            try:
                return hymn.number == int(query)
            except ValueError:
                return False

        return [hymn for hymn in HYMNS if matches(hymn)]

    def _on_search_change(self, e: ft.Event[ft.TextField]) -> None:
        self.search_query = e.control.value or ""
        self._render_current_route()

    def _on_nav_change(self, e: ft.Event[ft.NavigationBar]) -> None:
        routes = ["/home", "/favorites", "/settings"]
        self.page.go(routes[e.control.selected_index])

    def _toggle_favorite_and_refresh(self, hymn_id: int) -> None:
        if hymn_id in self.favorite_ids:
            self.favorite_ids.remove(hymn_id)
        else:
            self.favorite_ids.add(hymn_id)

        self._save_favorites()
        self._render_current_route()

    def _on_theme_change(self, e: ft.Event[ft.Dropdown]) -> None:
        if e.control.value not in _THEME_BY_NAME:
            return

        self.theme_name = e.control.value
        self.page.theme_mode = _THEME_BY_NAME[self.theme_name]
        self._save_theme()
        self._render_current_route()

    def _on_font_size_change(self, e: ft.Event[ft.Slider]) -> None:
        self.font_size = float(e.control.value or self.font_size)
        self._save_font_size()
        self._render_current_route()


def build_app(page: ft.Page) -> None:
    app = HymnApp(page)
    app.setup()
