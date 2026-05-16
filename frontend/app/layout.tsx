import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "HireSense AI",
  description: "AI Resume & Job Fit Analyzer",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
