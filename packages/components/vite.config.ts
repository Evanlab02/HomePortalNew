/* eslint-disable @typescript-eslint/no-unsafe-argument */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-call */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
import { resolve, join } from "path";
import { readdirSync, statSync } from "fs";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import dts from "vite-plugin-dts";


function getEntries(dir: string) {
	const entries: Record<string, string> = {};

	function walk(dir: string) {
		const files = readdirSync(dir);

		files.forEach((file: string) => {
			const fullPath = join(dir, file);
			const stat = statSync(fullPath);
			const isTestFile = fullPath.endsWith(".test.tsx") || fullPath.endsWith(".test.ts") || fullPath.endsWith(".snap") || fullPath.endsWith("vitest.config.ts");

			if (stat.isDirectory()) {
				walk(fullPath);
			} else if (stat.isFile() && !isTestFile) {
				const name = fullPath.replace(/^src\//, "").replace(/\.tsx?$/, "");
				entries[name] = fullPath;
			}
		});
	}

	walk(dir);
	return entries;
}

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [
		react(),
		dts({
			tsconfigPath: "tsconfig.app.json",
			entryRoot: "src"
		})
	],
	build: {
		outDir: "lib",
		lib: {
			entry: resolve(__dirname, "src/index.ts"),
			name: "HomePortalComponents",
			formats: ["es", "cjs"],
			fileName: "index.cjs"
		},
		rollupOptions: {
			input: {
				...getEntries("src")
			},
			output: {
				preserveModules: true,
				dir: "lib",
				entryFileNames: "[name].[format].cjs",
				chunkFileNames: "[name].[format].cjs"
			},
			external: [
				"react",
				"react-dom",
				"antd",
				"@ant-design/icons",
				"vitest-fetch-mock",
				"vitest",
				"@vitest"
			]
		}
	}
});
