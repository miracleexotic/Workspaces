import { createBrowserRouter, RouterProvider } from "react-router-dom";

import ForescoutRedirectPage from "./Pages/ForescoutRedirect";

function AppRouter() {
  const router = createBrowserRouter([
    {
      path: "/php/uid.php",
      element: <ForescoutRedirectPage />,
    },
  ]);

  return (
    <div>
      <RouterProvider router={router}></RouterProvider>
    </div>
  );
}

export default AppRouter;
