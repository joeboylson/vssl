import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Routes } from "../enums/routes";
import Home from "../pages/Home";
import Header from "../components/Header";
import { WithSTLInputContext } from "../context/STLInputs";
import AuthenticatedWrapper from "../components/AuthenticatedWrapper";
import Login from "../pages/Login";

const router = createBrowserRouter([
  {
    path: Routes.LOGIN,
    element: <Login />,
  },
  {
    path: Routes.ROOT,
    element: (
      <AuthenticatedWrapper>
        <Home />
      </AuthenticatedWrapper>
    ),
  },
]);

export function Router() {
  return (
    <WithSTLInputContext>
      <RouterProvider router={router} />
    </WithSTLInputContext>
  );
}
