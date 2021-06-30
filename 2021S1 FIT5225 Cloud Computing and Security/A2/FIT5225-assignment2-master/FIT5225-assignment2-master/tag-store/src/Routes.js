import React from "react";
import { Route, Switch } from "react-router-dom";
import SignIn from "./containers/sign-in";
import SignUp from "./containers/SignUp";
import Home from "./containers/Home";
import NotFound from "./containers/NotFound";
import Upload from "./containers/Upload";
import Navigation from "./containers/Navigation";
import Query from "./containers/Query";
import AuthenticatedRoute from "./containers/AuthenticatedRoute";
import UnauthenticatedRoute from "./containers/UnauthenticatedRoute";

export default function Routes() {
  return (
    <Switch>
      <UnauthenticatedRoute exact path="/">
        <Home />
      </UnauthenticatedRoute>
      <UnauthenticatedRoute exact path="/SignIn">
        <SignIn />
      </UnauthenticatedRoute>
      <UnauthenticatedRoute exact path="/SignUp">
        <SignUp />
      </UnauthenticatedRoute>
      <AuthenticatedRoute exact path="/Upload">
        <Upload />
      </AuthenticatedRoute>
      <AuthenticatedRoute exact path="/Query">
        <Query />
      </AuthenticatedRoute>
      <AuthenticatedRoute>
        <Route exact path="/Navigation">
          <Navigation />
        </Route>
      </AuthenticatedRoute>
      <AuthenticatedRoute>
        <NotFound />
      </AuthenticatedRoute>
    </Switch>
  );
}