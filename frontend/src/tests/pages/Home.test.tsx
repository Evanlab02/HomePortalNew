import { render } from "@testing-library/react";
import { beforeEach, expect, test } from "vitest";
import Home from "../../pages/Home";
import { appData } from "../mock/ApplicationData.mock";

beforeEach(() => {
	document.getElementsByTagName("html")[0].innerHTML = "";
});

test("Home page renders correctly", async () => {
	fetchMock.mockResponseOnce(JSON.stringify(appData));

	const { findByTestId } = render(
		<Home />
	);

	const home = await findByTestId("hp-home-page");
	expect(home).toMatchSnapshot();
});