# In productivity.py


# class ProductivitySystem:
#     def track(self, employees, hours):
#         print('Tracking Employee Productivity')
#         print('==============================')
#         for employee in employees:
#             result = employee.work(hours)
#             print(f'{employee.name}: {result}')
#         print('')


class ProductivitySystem:
    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('role_id')
        return role_type()

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')

# The ProductivitySystem tracks productivity based on employee roles. There are different employee roles:

# Managers: They walk around yelling at people telling them what to do. They are salaried employees and make more money.
# Secretaries: They do all the paper work for managers and ensure that everything gets billed and payed on time. They are also salaried employees but make less money.
# Sales employees: They make a lot of phone calls to sell products. They have a salary, but they also get commissions for sales.
# Factory workers: They manufacture the products for the company. They are paid by the hour.


# class ManagerRole:
#     def work(self, hours):
#         return f'screams and yells for {hours} hours.'


# class SecretaryRole:
#     def work(self, hours):
#         return f'expends {hours} hours doing office paperwork.'


# class SalesRole:
#     def work(self, hours):
#         return f'expends {hours} hours on the phone.'


# class FactoryRole:
#     def work(self, hours):
#         return f'manufactures gadgets for {hours} hours.'


class ManagerRole:
    def perform_duties(self, hours):
        return f'screams and yells for {hours} hours.'


class SecretaryRole:
    def perform_duties(self, hours):
        return f'does paperwork for {hours} hours.'


class SalesRole:
    def perform_duties(self, hours):
        return f'expends {hours} hours on the phone.'


class FactoryRole:
    def perform_duties(self, hours):
        return f'manufactures gadgets for {hours} hours.'
