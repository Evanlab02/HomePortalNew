import { PropsWithChildren } from "react";

export default function FlexGridContainer(props: Readonly<PropsWithChildren>) {
	const { children } = props;

	return (
		<div data-testid="hp-flex-grid-container" className="hp-flex-grid-container">
			{children}
		</div>
	);
}