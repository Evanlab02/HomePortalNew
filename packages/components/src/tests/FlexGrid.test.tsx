import { render } from "@testing-library/react";
import { expect, test } from "vitest";
import FlexGridContainer from "../FlexGrid";
import FlexGridItem from "../FlexGrid/FlexGridItem";

test("Flex grid renders correctly", async () => {
	const { findByTestId } = render(
		<FlexGridContainer>
			<FlexGridItem xs={1} sm={2} md={3} lg={4} xl={5} xxl={6}>
				<p>Hello World!</p>
			</FlexGridItem>
		</FlexGridContainer>
	);

	const flexContainer = await findByTestId("hp-flex-grid-container");
	expect(flexContainer).toMatchSnapshot();
});