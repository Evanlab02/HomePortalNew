import { Menu, MenuProps } from "antd";

type AntMenuClick = Required<MenuProps>["onClick"];
export type NavMenuItem = Required<MenuProps>["items"][number];

export interface NavMenuProps {
    items: NavMenuItem[];
    onClickCallback?: (key: string) => void;
}

export default function NavMenu(props: Readonly<NavMenuProps>) {
	const {
		items,
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
			mode="horizontal"
			theme="dark"
		/>
	);
}