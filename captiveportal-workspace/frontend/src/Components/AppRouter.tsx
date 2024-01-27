import { createBrowserRouter, RouterProvider } from "react-router-dom";

import CaptivePortalPage from "./Pages/CaptivePortal";
import TermsConditionsPage from "./Pages/TermsConditions";
import WelcomePage from "./Pages/Welcome";

function AppRouter() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <CaptivePortalPage />,
    },
    {
      path: "/termsconditions",
      element: <TermsConditionsPage />,
    },
    {
      path: "/welcome",
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
