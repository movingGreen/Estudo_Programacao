import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Blogs from "./pages/Blogs";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <NoPage />,
    // loader: rootLoader,
    // action: rootAction,
    children: [
      {
        errorElement: <NoPage />,
        children: [
          { index: true, element: <Home /> },
          {
            path: "contact",
            element: <Contact />,
            // loader: contactLoader,
            // action: contactAction,
          },
          {
            path: "blogs",
            element: <Blogs />,
            // loader: contactLoader,
            // action: editAction,
          },
          // {
          //   path: "contacts/:contactId/destroy",
          //   action: destroyAction,
          //   errorElement: <div>Erro na ação de deletar um contato!</div>,
          // },
        ],
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
