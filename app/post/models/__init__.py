from .comment import Comment
from .post import Post, PostTags
from .tag import Tag 
from .SoftDeleteMixin import SoftDeleteMixin, SoftDeleteManager


# Esto hace que Django los detecte
__all__ = ['Comment', 'Post', 'Tag','SoftDeleteMixin', 'SoftDeleteManager', 'PostTags']