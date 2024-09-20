import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Routes } from "../enums/routes";
import { WithSTLInputContext } from "../context/STLInputs";
import Home from "../pages/Home";
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
