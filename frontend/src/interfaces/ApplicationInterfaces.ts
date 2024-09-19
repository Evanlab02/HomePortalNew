export interface HomePortalApplication {
    title: string;
    description: string;
    link_name: string;
    link: string;
}

export interface HomePortalApplications {
    applications: HomePortalApplication[]
}

export interface HomePortalNavMenuItem {
    link: string;
    nav_link_name: string;
    nav_link_icon: string;
}

export interface HomePortalNavMenuItems {
    applications: HomePortalNavMenuItem[];
}

export interface HomePortalSideMenuItem {
    link: string,
    side_menu_name: string,
    side_menu_icon: string
}

export interface HomePortalSideMenuCategory {
    category: string;
    icon: string;
    applications: HomePortalSideMenuItem[];
}

export interface HomePortalSideMenuItems {
    categories: HomePortalSideMenuCategory[];
    no_category: HomePortalSideMenuItem[];
}