from .middlewares import get_current_db_name

class Router:
    def db_for_read(self, model, **hints):
        """Reads go to a reading database."""
        return get_current_db_name()

    def db_for_write(self, model, **hints):
        """Writes always go to writing database."""
        return get_current_db_name()

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """

        db_list = ('read', 'write')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """All non-auth models end up in this pool."""
        return True
