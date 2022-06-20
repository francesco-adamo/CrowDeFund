import { Store } from '../store';

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/home.vue') }
    ],
    beforeEnter(to, from, next) {
      const authenticated = Store.state.user.authenticated;
      if (authenticated) next(from.fullPath); // prevent access once logged in
      else next(); // proceed
    }
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/404.vue')
  }
]

export default routes
