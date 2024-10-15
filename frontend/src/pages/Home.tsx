import { useEffect, useState } from "react";
import { FlexGridItem, FlexGrid, Card } from "@evanlab02/hp-react-components";
import { getApps } from "../api/ApplicationController";
import { HomePortalApplication } from "../interfaces/ApplicationInterfaces";
import "./styles/Home.scss";

export default function Home() {
	const [apps, setApps] = useState<HomePortalApplication[]>([]);

	useEffect(() => {
		void fetchApplications();
	}, []);

	const fetchApplications = async () => {
		const applications = await getApps();
		setApps(applications);
	};

	return (
		<div className="home-portal" data-testid="hp-home-page">
			<h1>Services</h1>
			<FlexGrid>
				{apps.map((app) => {
					return (
						<FlexGridItem xs={12} sm={12} md={12} lg={6} xl={4} xxl={2} key={`${app.title}-${app.link_name}`}>
							<Card
								title={app.title}
								extra={<a target="_blank" className="hp-service-link" href={app.link} rel="noreferrer">{app.link_name}</a>}
							>
								<p>{app.description}</p>
							</Card>
						</FlexGridItem>
					);
				})}
			</FlexGrid>
		</div>
	);
}