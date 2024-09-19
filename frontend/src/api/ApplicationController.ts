import { HomePortalApplications, HomePortalNavMenuItems, HomePortalSideMenuItems } from "../interfaces/ApplicationInterfaces";
import { getData } from "./BaseController";

export async function getApps() {
	const response = await getData("/apis/portal/api/v1/applications");
	const data = await response.json() as HomePortalApplications;
	return data.applications;
}

export async function getNavMenuApps() {
	const response = await getData("/apis/portal/api/v1/applications/navmenu");
	const data = await response.json() as HomePortalNavMenuItems;
	return data.applications;
}

export async function getSideMenuApps() {
	const response = await getData("/apis/portal/api/v1/applications/sidemenu");
	const data = await response.json() as HomePortalSideMenuItems;
	return data;
}