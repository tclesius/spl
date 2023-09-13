const isAuthenticated = () => {
    return !!localStorage.getItem("access_token"); // TODO: WARNING: highly experimental and probably wrong
};

const loginRouteGuard = (to, from, next) => {
    if (to.meta.requiresAuth && !isAuthenticated()) {
        next('/admin/login'); // Redirect to login page if not authenticated
    } else if (to.meta.requiresGuest && isAuthenticated()) {
        next('/admin/users'); // Proceed to the requested route
    } else {
        next()
    }
};

export default loginRouteGuard;
