"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Core
    Copyright (C) 2005-2017 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

from _version import get_versions

from django.conf import settings
from django.utils import timezone

from ESSArch_Core.configuration.models import (
    Agent,
    EventType,
    Parameter,
    Path,
)

from ESSArch_Core.configuration.serializers import (
    AgentSerializer,
    EventTypeSerializer,
    ParameterSerializer,
    PathSerializer,
)

from ESSArch_Core.util import (
    run_shell_command
)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class SysInfoView(APIView):
    """
    API endpoint that allows system info to be viewed
    """

    def get(self, request):
        context = {}
        cwd = settings.BASE_DIR

        # Shell commands: Name and command
        SHELL_COMMANDS = [
            ('hostname', 'hostname'),
            ('mysql_version', 'mysql --version'),
            ('python_packages', 'pip freeze'),
        ]

        # Flags in settings: Their expected  and actual values.
        SETTINGS_FLAGS = [
            ('DEBUG', False),
            ('LANGUAGE_CODE', None),
            ('TIME_ZONE', None),
        ]

        context['version'] = get_versions()['version']
        context['time_checked'] = timezone.now()

        for name, cmd in SHELL_COMMANDS:
            context[name] = run_shell_command(cmd, cwd)

        context['python_packages'] = context['python_packages'].split('\n')

        context['settings_flags'] = []
        for name, expected in SETTINGS_FLAGS:
            actual_setting = getattr(settings, name, None)
            if expected is not None:
                unexpected = expected != actual_setting
            else:
                unexpected = False
            context['settings_flags'].append({
                'name': name,
                'unexpected': unexpected,
                'actual': actual_setting
            })

        return Response(context)


class EventTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows event types to be viewed or edited.
    """
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    pagination_class = None


class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agents to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class ParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows parameters to be viewed or edited.
    """
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class PathViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows paths to be viewed or edited.
    """
    queryset = Path.objects.all()
    serializer_class = PathSerializer
