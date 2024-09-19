import { HEADERS } from "../constants/Constants";

export async function getData(url: string): Promise<Response> {
	const response = await fetch(url,
		{
			method: "GET",
			headers: HEADERS
		}
	);

	if (response.status == 401) {
		window.location.href = "/accounts/";
	}

	return response;
}