import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [react()],
	server: {
		open: "/",
		proxy: {
			"/apis/": {
				target: "http://localhost:80",
				changeOrigin: true
			}
		}
	}
});
