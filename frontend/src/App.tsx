import { useEffect, useState } from "react";
import { Outlet } from "react-router";
import { HomeOutlined, MenuOutlined } from "@ant-design/icons";
import { SideMenuItem, SideMenu, NavMenu, NavMenuItem, FlexGridItem, FlexGrid } from "@evanlab02/hp-react-components";
import { getNavMenuApps, getSideMenuApps } from "./api/ApplicationController";
import { iconMap } from "./constants/IconMap";
import { HomePortalNavMenuItem, HomePortalSideMenuCategory, HomePortalSideMenuItem } from "./interfaces/ApplicationInterfaces";
import Navigation from "./routes/Navigation";
import "@evanlab02/hp-react-components/lib/FlexGrid/styles/index.css";
import "@evanlab02/hp-react-components/lib/SideMenu/styles/index.css";
import "@evanlab02/hp-react-components/lib/NavMenu/styles/index.css";
import "./styles/App.scss";

export default function App() {
	const [isMenuOpen, setIsMenuOpen] = useState(false);
	const [navMenuItems, setNavMenuItems] = useState<HomePortalNavMenuItem[]>([]);
	const [sideMenuCategories, setSideMenuCategories] = useState<HomePortalSideMenuCategory[]>([]);
	const [sideMenuItems, setSideMenuItems] = useState<HomePortalSideMenuItem[]>([]);

	useEffect(() => {
		void fetchNavMenuItems();
		void fetchSideMenuItems();
	}, []);

	const fetchNavMenuItems = async () => {
		const applications = await getNavMenuApps();
		setNavMenuItems(applications);
	};

	const fetchSideMenuItems = async () => {
		const applications = await getSideMenuApps();
		setSideMenuCategories(applications.categories);
		setSideMenuItems(applications.no_category);
	};

	const navItems: NavMenuItem[] = [
		{
			key: "menu",
			label: "Menu",
			icon: <MenuOutlined />,
			onClick: () => { setIsMenuOpen((prev) => !prev); }
		},
		{
			key: "home",
			label: "Home",
			icon: <HomeOutlined />,
			onClick: () => { window.location.href = "/"; }
		},
		...navMenuItems.map((app) => {
			return {
				key: app.nav_link_name.toLowerCase(),
				label: app.nav_link_name,
				icon: iconMap.get(app.nav_link_icon),
				onClick: () => { window.location.href = app.link; }
			} as NavMenuItem;
		})
	];

	const items: SideMenuItem[] = [
		{
			key: "home",
			label: "Home",
			icon: <HomeOutlined />,
			onClick: () => { window.location.href = "/"; }
		},
		...sideMenuCategories.map((category) => {
			return {
				key: category.category.toLowerCase(),
				label: category.category,
				icon: iconMap.get(category.icon),
				children: [
					...category.applications.map((app) => {
						return {
							key: app.side_menu_name.toLowerCase(),
							label: app.side_menu_name,
							icon: iconMap.get(app.side_menu_icon),
							onClick: () => { window.location.href = app.link; }
						} as SideMenuItem;
					})
				]
			} as SideMenuItem;
		}),
		...sideMenuItems.map((item) => {
			return {
				key: item.side_menu_name.toLowerCase(),
				label: item.side_menu_name,
				icon: iconMap.get(item.side_menu_icon),
				onClick: () => { window.location.href = item.link; }
			} as SideMenuItem;
		})
	];

	return (
		<div className="home-portal-app" data-testid="hp-app">
			<div className="home-portal-side-menu">
				<SideMenu
					items={items}
					isOpen={isMenuOpen}
				/>
			</div>
			<div className="home-portal-content">
				<FlexGrid>
					<FlexGridItem xs={12} sm={12} md={12} lg={12} xl={12} xxl={12}>
						<NavMenu
							items={navItems}
						/>
					</FlexGridItem>
					<FlexGridItem xs={12} sm={12} md={12} lg={12} xl={12} xxl={12}>
						<Navigation />
						<Outlet />
					</FlexGridItem>
				</FlexGrid>
			</div>
		</div>
	);
}
