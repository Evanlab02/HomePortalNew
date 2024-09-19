import { Card, ConfigProvider, ThemeConfig } from "antd";
import { PropsWithChildren, ReactNode } from "react";

const theme: ThemeConfig = {
	token: {
		colorPrimary: "#1677ff",
		colorText: "#fff"
	},
	components: {
		Card: {
			colorBgContainer: "#001529",
			colorBorderSecondary: "rgba(255, 255, 255, 0.65)"
		}
	}
};

export interface CardProps extends PropsWithChildren {
    title: string;
    extra?: ReactNode;
}

export default function HpCard(props: Readonly<CardProps>) {
	const { title, extra, children } = props;

	return (
		<ConfigProvider theme={theme}>
			<Card
				title={title}
				extra={extra}
			>
				{children}
			</Card>
		</ConfigProvider>
	);
}