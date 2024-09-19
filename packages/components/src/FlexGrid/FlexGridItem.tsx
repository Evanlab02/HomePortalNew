import { PropsWithChildren } from "react";

export interface FlexGridItemProps extends PropsWithChildren {
    xs?: number
    sm?: number
    md?: number
    lg?: number
    xl?: number
    xxl?: number
}

export default function FlexGridItem(props: Readonly<FlexGridItemProps>) {
	const { children, xs, sm, md, lg, xl, xxl } = props;

	const classes = [
		xs && `hp-flex-grid-col-xs-${xs.toString()}`,
		sm && `hp-flex-grid-col-sm-${sm.toString()}`,
		md && `hp-flex-grid-col-md-${md.toString()}`,
		lg && `hp-flex-grid-col-lg-${lg.toString()}`,
		xl && `hp-flex-grid-col-xl-${xl.toString()}`,
		xxl && `hp-flex-grid-col-xxl-${xxl.toString()}`
	].filter(Boolean).join(" ");

	return (
		<div className={classes} data-testid="hp-flex-grid-item">
			{children}
		</div>
	);
}