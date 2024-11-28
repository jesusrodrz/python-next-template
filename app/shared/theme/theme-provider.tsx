"use client";
import { CssVarsProvider, extendTheme } from "@mui/joy/styles";
import { theme } from "./theme";

type ThemeProviderProps = {
  children: React.ReactNode;
};

export function ThemeProvider({ children }: ThemeProviderProps) {
  return <CssVarsProvider theme={theme}>{children}</CssVarsProvider>;
}
