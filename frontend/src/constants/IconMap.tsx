import { ReactNode } from "react";
import { CodeFilled, DatabaseOutlined, HomeOutlined, MenuOutlined, TeamOutlined, UserOutlined, BookOutlined, DesktopOutlined, CheckSquareOutlined } from "@ant-design/icons";

export const iconMap = new Map<string, ReactNode>();
iconMap.set("MenuOutlined", <MenuOutlined />);
iconMap.set("CodeFilled", <CodeFilled />);
iconMap.set("DatabaseOutlined", <DatabaseOutlined />);
iconMap.set("HomeOutlined", <HomeOutlined />);
iconMap.set("TeamOutlined", <TeamOutlined />);
iconMap.set("UserOutlined", <UserOutlined />);
iconMap.set("BookOutlined", <BookOutlined />);
iconMap.set("DesktopOutlined", <DesktopOutlined />);
iconMap.set("CheckSquareOutlined", <CheckSquareOutlined />);
