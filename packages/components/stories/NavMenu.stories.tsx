import React from "react";
import type { Meta, StoryObj } from "@storybook/react";
import { ContainerOutlined, DesktopOutlined, MailOutlined, PieChartOutlined } from "@ant-design/icons";
import NavMenu from "../src/NavMenu";

const meta: Meta<typeof NavMenu> = {
	component: NavMenu,
	parameters: {
		backgrounds: {
			default: "dark"
		}
	},
	decorators: [
		(Story) => (
			<div style={{ width: "1800px", height: "1000px" }}>
				<Story />
			</div>
		)
	]
};

export default meta;
type Story = StoryObj<typeof NavMenu>;

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
		onClickCallback: undefined
	}
};
