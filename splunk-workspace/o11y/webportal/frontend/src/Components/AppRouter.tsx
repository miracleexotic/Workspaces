import { createBrowserRouter, RouterProvider } from "react-router-dom";

import WelcomePage from "./Pages/Welcome";

function AppRouter() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <WelcomePage />,
    },
  ]);

  return (
    <div>
      <RouterProvider router={router}></RouterProvider>
    </div>
  );
}

export default AppRouter;
