import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
	plugins: [react()],
	test: {
		environment: "jsdom",
		reporters: ["html", "default"],
		coverage: {
			provider: "v8",
			reporter: ["text", "json", "html", "lcov"],
			include: ["src/**/*.tsx", "src/**/*.ts"],
			exclude: ["src/tests/*", "src/main.tsx", "src/vite-env.d.ts"]
		},
		setupFiles: [
			"./src/setupVitest.ts"
		]
	},
});