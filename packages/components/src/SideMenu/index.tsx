import { Menu, MenuProps } from "antd";

type AntMenuClick = Required<MenuProps>["onClick"];
export type SideMenuItem = Required<MenuProps>["items"][number];

export interface SideMenuProps {
	items: SideMenuItem[];
	isOpen?: boolean;
	defaultOpenKeys?: string[];
	onClickCallback?: (key: string) => void;
}

export default function SideMenu(props: Readonly<SideMenuProps>) {
	const {
		items,
		isOpen = true,
		defaultOpenKeys,
		onClickCallback
	} = props;

	const onClick: AntMenuClick = (menu) => {
		if (onClickCallback)
			onClickCallback(menu.key);
	};

	return (
		<Menu
			items={items}
			onClick={onClick}
			mode="inline"
			inlineCollapsed={!isOpen}
			theme="dark"
			defaultOpenKeys={defaultOpenKeys}
		/>
	);
}