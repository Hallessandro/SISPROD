from django.db import transaction,IntegrityError

from appprod.models import Cargo

cargo1 = Cargo(descricao='vendedor',salario=880)
cargo2 = Cargo(descricao='produtor',salario=1180)

cargo1.save()
cargo2.save()



