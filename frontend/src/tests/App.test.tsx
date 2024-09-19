import { render } from "@testing-library/react";
import { beforeEach, expect, test } from "vitest";
import { appData } from "./mock/ApplicationData.mock";
import { navMenuMock } from "./mock/NavMenuData.mock";
import { sideMenuMock } from "./mock/SideMenuData.mock";
import App from "../App";
import { MemoryRouter } from "react-router";

beforeEach(() => {
	document.getElementsByTagName("html")[0].innerHTML = "";
});

test("App renders correctly", async () => {
	fetchMock.mockResponseOnce(JSON.stringify(appData));
	fetchMock.mockResponseOnce(JSON.stringify(navMenuMock));
	fetchMock.mockResponseOnce(JSON.stringify(sideMenuMock));

	const { findByTestId } = render(
		<MemoryRouter initialEntries={[""]}>
			<App />
		</MemoryRouter>
	);

	const app = await findByTestId("hp-app");
	expect(app).toMatchSnapshot();
});