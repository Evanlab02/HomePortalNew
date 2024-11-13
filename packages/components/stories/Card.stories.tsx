import React from "react";
import type { Meta, StoryObj } from "@storybook/react";
import HpCard from "../src/Card";

const meta: Meta<typeof HpCard> = {
	component: HpCard,
	parameters: {
		backgrounds: {
			default: "dark"
		}
	}
};

export default meta;
type Story = StoryObj<typeof HpCard>;

export const Default: Story = {
	args: {
		title: "Home Portal Card",
		extra: <a>Extra Elements</a>,
		children: <p>This is a home portal card.</p>
	}
};
