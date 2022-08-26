from peewee import PostgresqlDatabase


class DatabaseManagment:

    def __init__(self):
        self.databese = self.postgresql_database_connection()

    def __enter__(self):
        """
        This Method Provides Database Connection Process Before Requests
        :return:
        """
        self.databese.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        This Method Provides Database Connection Close Process After Requests
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.databese.close()

    def postgresql_database_connection(self) -> PostgresqlDatabase:
        """
        This Function Provide Connection To FastAPI Basic Postgresql Database.
        :return: models connection
        """
        try:
            databese = PostgresqlDatabase(
                database="my-blog",
                user="postgres",
                password="090816",
                host="localhost",
                port=5432
            )

            return databese
        except Exception as error:
            print(error)

    def postgresql_create_tables(self):
        """
        This Method Creates Necessary Postgresql Models For FastAPI Basic
        :return:
        """
        from app.models.contact_request import ContactRequest

        try:
            with self.databese as database:
                database.create_tables(
                    [ContactRequest]
                )

                return True
        except Exception as error:
            print(error)

            return False
