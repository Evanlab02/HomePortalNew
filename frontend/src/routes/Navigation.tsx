import { Route, Routes } from "react-router";
import Home from "../pages/Home";

export default function Navigation() {
	return (
		<Routes>
			<Route path="" element={<Home />} />
		</Routes>
	);
}