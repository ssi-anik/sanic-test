from orator.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('name', 40)
            table.string('email', 50)
            table.string('password', 64)
            table.timestamps()

    def down(self):
        self.schema.drop('users')
