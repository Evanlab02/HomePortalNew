import React, { useState } from "react";
import type { Meta, StoryObj } from "@storybook/react";
import { ContainerOutlined, DesktopOutlined, MailOutlined, PieChartOutlined } from "@ant-design/icons";
import "../src/SideMenu/styles/index.scss";

import SideMenu, { SideMenuProps } from "../src/SideMenu";
import { Button } from "antd";

const meta: Meta<typeof SideMenu> = {
	component: SideMenu,
	parameters: {
		backgrounds: {
			default: "dark"
		}
	},
	decorators: [
		(Story) => (
			<div style={{ width: "300px", height: "800px" }}>
				<Story />
			</div>
		)
	]
};

export default meta;
type Story = StoryObj<typeof SideMenu>;

export const Default: Story = {
	args: {
		items: [
			{
				key: "item-1",
				label: "Item #1",
				icon: <PieChartOutlined />
			},
			{
				key: "item-2",
				label: "Item #2",
				icon: <DesktopOutlined />
			},
			{
				key: "item-3",
				label: "Item #3",
				icon: <ContainerOutlined />,
				children: [
					{ key: "5", label: "Option 4" },
					{ key: "6", label: "Option 5" },
					{ key: "7", label: "Option 6" },
				]
			},
			{
				key: "item-7",
				label: "Item #7",
				icon: <MailOutlined />
			}
		],
		defaultOpenKeys: undefined,
		isOpen: undefined,
		onClickCallback: undefined
	}
};

const StoryRender1 = (args: SideMenuProps) => {
	const [isOpen, setIsOpen] = useState(false);

	return (
		<div style={{ width: "300px", height: "800px" }}>
			<Button
				type="primary"
				onClick={() => { setIsOpen((prev) => !prev); }}
			>
				{isOpen ? "Close" : "Open"}
			</Button>
			<SideMenu
				isOpen={isOpen}
				{...args}
			/>
		</div>
	);
};

export const MenuWithButton: Story = {
	args: {
		items: [
			{
				key: "item-1",
				label: "Item #1",
				icon: <PieChartOutlined />
			},
			{
				key: "item-2",
				label: "Item #2",
				icon: <DesktopOutlined />
			},
			{
				key: "item-3",
				label: "Item #3",
				icon: <ContainerOutlined />,
				children: [
					{ key: "5", label: "Option 4" },
					{ key: "6", label: "Option 5" },
					{ key: "7", label: "Option 6" },
				]
			},
			{
				key: "item-7",
				label: "Item #7",
				icon: <MailOutlined />
			}
		],
		defaultOpenKeys: undefined,
		onClickCallback: undefined
	},
	render: StoryRender1
};