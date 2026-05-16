"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

import { getToken, logout } from "@/lib/api";

type AppNavbarProps = {
  publicMode?: boolean;
};

export default function AppNavbar({ publicMode = false }: AppNavbarProps) {
  const pathname = usePathname();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    setIsLoggedIn(Boolean(getToken()));
  }, []);

  function isActive(path: string) {
    return pathname === path;
  }

  const loggedInLinks = [
    { label: "Dashboard", href: "/dashboard" },
    { label: "History", href: "/history" },
    { label: "Metrics", href: "/accuracy" },
    { label: "About", href: "/about" },
  ];

  return (
    <nav className="nav">
      <Link href="/" className="logo">
        HireSense AI
      </Link>

      <div className="nav-links">
        {isLoggedIn ? (
          <>
            {loggedInLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className={`btn ${isActive(link.href) ? "btn-active" : ""}`}
              >
                {link.label}
              </Link>
            ))}

            <button className="btn btn-danger" onClick={logout}>
              Logout
            </button>
          </>
        ) : (
          <>
            {!publicMode && (
              <Link
                href="/"
                className={`btn ${isActive("/") ? "btn-active" : ""}`}
              >
                Home
              </Link>
            )}

            <Link
              href="/about"
              className={`btn ${isActive("/about") ? "btn-active" : ""}`}
            >
              Documentation
            </Link>

            <Link
              href="/login"
              className={`btn ${isActive("/login") ? "btn-active" : ""}`}
            >
              Login
            </Link>

            <Link href="/register" className="btn btn-primary">
              Get Started
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}
