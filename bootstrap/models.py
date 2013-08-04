from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import ugettext_lazy as _, ugettext

from betterforms.forms import BetterModelForm

import widgy
from widgy.models import Content
from widgy.contrib.page_builder.models import Layout, Bucket


CONTEXT_STATE_CHOICES = (
    (_('primary'), _('Primary')),
    (_('success'), _('Success')),
    (_('warning'), _('Warning')),
    (_('danger'), _('Danger')),
    (_('info'), _('Info')),
)


def choices_with_blank(choices, blank_choice=None):
    if blank_choice is None:
        blank_choice = ('', '-----------')
    return (blank_choice,) + tuple(choices)


class BootstrapClassMixin(object):
    css_classes = []

    @classmethod
    def get_template_kwargs(cls, **kwargs):
        defaults = {
            'app_label': 'bootstrap',
            'module_name': 'div_with_classes',
        }
        defaults.update(**kwargs)

        return super(BootstrapClassMixin, cls).get_template_kwargs(**kwargs) + [defaults]

    def css_classes_for_render(self):
        return ' '.join(self.css_classes)


@widgy.register
class GridRow(BootstrapClassMixin, Bucket):
    css_classes = ('row',)

    deletable = True
    draggable = True

    def valid_parent_of(self, cls, obj=None):
        return issubclass(cls, (GridSpan,))

    class Meta:
        verbose_name = _('row')
        verbose_name_plural = _('rows')


class GridSpanForm(BootstrapClassMixin, BetterModelForm):
    def clean(self):
        cd = super(GridSpanForm, self).clean()
        span = cd.get('span') or 0
        offset = cd.get('offset') or 0
        if span + offset > 12:
            self.form_error('`span` and `offset` cannot total greater than 12')
        return cd


@widgy.register
class GridSpan(BootstrapClassMixin, Bucket):
    span = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=True)
    offset = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], null=True, blank=True)

    form = GridSpanForm
    editable = True
    deletable = True
    draggable = True

    class Meta:
        verbose_name = _('span')
        verbose_name_plural = _('spans')

    def __unicode__(self):
        if not self.span:
            return u"Span"
        elif self.offset:
            return u"Span {s.span} - Offset {s.offset}".format(s=self)
        return u"Span {s.span}".format(s=self)

    def valid_parent_of(self, cls, obj=None):
        return not issubclass(cls, (GridSpan,))

    @property
    def css_classes(self):
        class_list = []
        if self.span:
            class_list.append("span{s.span}".format(s=self))
        if self.offset:
            class_list.append("offset{s.span}".format(s=self))
        return class_list


@widgy.register
class Well(BootstrapClassMixin, Bucket):
    css_classes = ('well',)

    deletable = True
    draggable = True

    def valid_parent_of(self, cls, obj=None):
        return not issubclass(cls, (Well, GridSpan, GridRow,))

    class Meta:
        verbose_name = _('well')
        verbose_name_plural = _('wells')


@widgy.register
class Jumbotron(BootstrapClassMixin, Bucket):
    css_classes = ('jumbotron',)

    deletable = True
    draggable = True

    class Meta:
        verbose_name = _('jumbotron')
        verbose_name_plural = _('jumbotron')


@widgy.register
class Panel(BootstrapClassMixin, Bucket):
    type = models.CharField(max_length='20', blank=True,
                            choices=choices_with_blank(CONTEXT_STATE_CHOICES))

    editable = True
    deletable = True
    draggable = True
    shelf = True

    class Meta:
        verbose_name = _('panel')
        verbose_name_plural = _('panel')

    @property
    def css_classes(self):
        css_classes = ['panel']
        if self.type is not None:
            css_classes.append('panel-{s.type}'.format(s=self))
        return css_classes


class SingletonPanelChild(object):
    @classmethod
    def valid_child_of(cls, parent, obj=None):
        if cls in (type(child) for child in parent.get_children()):
            return False
        return isinstance(parent, Panel)


@widgy.register
class PanelHeading(BootstrapClassMixin, SingletonPanelChild, Bucket):
    css_classes = ('panel-heading',)

    deletable = True
    draggable = True


@widgy.register
class PanelFooter(BootstrapClassMixin, SingletonPanelChild, Bucket):
    css_classes = ('panel-heading',)

    deletable = True
    draggable = True
