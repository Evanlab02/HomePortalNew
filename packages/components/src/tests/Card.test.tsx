import { render } from "@testing-library/react";
import { expect, test } from "vitest";
import Card from "../Card";

test("Card renders correctly", async () => {
	const { findByTestId } = render(
		<div data-testid="testing-hp-card">
			<Card
				title="Hello World"
				extra={<a href="/link/to/somewhere">Random Link</a>}
			>
				<p>This is the card description, and goodbye world!</p>
			</Card>
		</div>
	);

	const card = await findByTestId("testing-hp-card");
	expect(card).toMatchSnapshot();
});