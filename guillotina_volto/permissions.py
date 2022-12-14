from guillotina import configure


configure.role("guillotina.Contributor", "Contributor", "Can add content", True)

configure.permission(
    "guillotina.ManageVersioning", "Ability to modify versioning on an object"
)
configure.permission(
    "guillotina.ManageConstraints", "Allow to check and change type constraints"
)

configure.permission("guillotina.AccessControlPanel", "Access control panel")
configure.permission("guillotina.ReviewContent", "Review content permission")
configure.permission("guillotina.RequestReview", "Request review content permission")

configure.permission("guillotina.ViewComments", "View comments")
configure.permission("guillotina.ModifyComments", "Modify comments")
configure.permission("guillotina.AddComments", "Add comments")
configure.permission("guillotina.DeleteComments", "Delete comments")
configure.permission("guillotina.DeleteAllComments", "Delete all comments")

configure.grant(permission="guillotina.ManageVersioning", role="guillotina.Manager")

configure.grant(permission="guillotina.ManageConstraints", role="guillotina.Manager")

configure.grant(
    permission="guillotina.ManageConstraints", role="guillotina.ContainerAdmin"
)

configure.grant(permission="guillotina.ReviewContent", role="guillotina.Reviewer")

configure.grant(permission="guillotina.ReviewContent", role="guillotina.Manager")

configure.grant(permission="guillotina.RequestReview", role="guillotina.Manager")

configure.grant(permission="guillotina.RequestReview", role="guillotina.Owner")

configure.grant(permission="guillotina.RequestReview", role="guillotina.ContainerAdmin")
configure.grant(
    permission="guillotina.AccessControlPanel", role="guillotina.ContainerAdmin"
)

configure.grant(permission="guillotina.SearchContent", role="guillotina.Manager")

configure.grant(permission="guillotina.ViewComments", role="guillotina.Manager")

configure.grant(permission="guillotina.AddComments", role="guillotina.Manager")

configure.grant(permission="guillotina.ModifyComments", role="guillotina.Manager")

configure.grant(permission="guillotina.DeleteComments", role="guillotina.Manager")

configure.grant(permission="guillotina.DeleteAllComments", role="guillotina.Manager")

configure.grant(permission="guillotina.ViewComments", role="guillotina.Owner")

configure.grant(permission="guillotina.AddComments", role="guillotina.Owner")

configure.grant(permission="guillotina.ModifyComments", role="guillotina.Owner")

configure.grant(permission="guillotina.DeleteComments", role="guillotina.Owner")

configure.grant(permission="guillotina.DeleteAllComments", role="guillotina.Owner")

configure.grant(permission="guillotina.AddContent", role="guillotina.Contributor")
configure.grant(permission="guillotina.AccessContent", role="guillotina.Contributor")
configure.grant(permission="guillotina.ViewContent", role="guillotina.Contributor")
