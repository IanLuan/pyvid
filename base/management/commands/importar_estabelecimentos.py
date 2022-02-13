from django.core.management.base import BaseCommand, CommandError
import os
import json

from base.models import EstabelecimentoSaude


class Command(BaseCommand):
    help = 'Importar estabelecimentos de saúde'

    def handle(self, *args, **options):
        json_path = os.path.join('base', 'fixtures', 'estabelecimentos.json')

        with open(json_path) as f:
            data = json.load(f)
            for estabelecimento in data:
                obj = {
                    'cnes': estabelecimento['CO_CNES'],
                    'nome_fantasia': estabelecimento['NO_FANTASIA']
                }
                EstabelecimentoSaude.objects.create(**obj)

