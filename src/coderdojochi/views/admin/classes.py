import operator
from collections import Counter

from django.db.models import Case, Count, IntegerField, When
from django.utils import timezone
from django.views.generic.list import ListView

from coderdojochi.models import Order, Session


class AdminClassesListView(ListView):

    model = Session

    template_name = 'admin_classes_list.html'

    def get_context_data(self, **kwargs):
        context = super(AdminClassesListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()

        context['object_list'] = Session.objects.select_related().annotate(
            num_orders=Count(
                'order'
            ),

            num_attended=Count(
                Case(
                    When(
                        order__check_in__isnull=False,
                        then=1
                    )
                )
            ),

            is_future=Case(
                When(
                    end_date__gte=timezone.now(),
                    then=1
                ),
                default=0,
                output_field=IntegerField(),
            )
        ).order_by(
            '-start_date'
        )

        orders = Order.objects.select_related()

        total_past_orders = orders.filter(is_active=True)
        context['total_past_orders_count'] = total_past_orders.count()
        total_checked_in_orders = orders.filter(
            is_active=True,
            check_in__isnull=False
        )
        context['total_checked_in_orders_count'] = total_checked_in_orders.count()

        context['upcoming_sessions'] = orders.filter(
            is_active=True,
            session__end_date__gte=timezone.now()
        ).order_by('session__start_date')

        # Genders
        context['gender_count'] = list(
            Counter(
                e.student.get_clean_gender() for e in total_checked_in_orders
            ).iteritems()
        )
        context['gender_count'] = sorted(
            dict(context['gender_count']).items(),
            key=operator.itemgetter(1)
        )

        # Ages
        ages = sorted(
            list(
                e.student.get_age() for e in total_checked_in_orders
            )
        )
        context['age_count'] = sorted(
            dict(
                list(
                    Counter(ages).iteritems()
                )
            ).items(),
            key=operator.itemgetter(0)
        )

        # Average Age
        context['average_age'] = int(
            round(
                sum(ages) / float(len(ages))
            )
        )

        return context
