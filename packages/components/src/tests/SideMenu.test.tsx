import { render } from "@testing-library/react";
import { expect, test } from "vitest";
import { ContainerOutlined, DesktopOutlined, MailOutlined, PieChartOutlined } from "@ant-design/icons";
import SideMenu from "../SideMenu";

test("Side menu renders correctly", async () => {
	const { findByTestId } = render(
		<div data-testid="side-menu-renders-correctly">
			<SideMenu
				items={[
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
				]}
				defaultOpenKeys={undefined}
				isOpen={undefined}
				onClickCallback={undefined}
			/>
		</div>
	);

	const nav = await findByTestId("side-menu-renders-correctly");
	expect(nav).toMatchSnapshot();
});