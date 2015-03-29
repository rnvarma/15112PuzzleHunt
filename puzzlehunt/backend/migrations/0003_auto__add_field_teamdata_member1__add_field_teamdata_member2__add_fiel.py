# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TeamData.member1'
        db.add_column(u'backend_teamdata', 'member1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'TeamData.member2'
        db.add_column(u'backend_teamdata', 'member2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'TeamData.member3'
        db.add_column(u'backend_teamdata', 'member3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'TeamData.member4'
        db.add_column(u'backend_teamdata', 'member4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'TeamData.team_name'
        db.add_column(u'backend_teamdata', 'team_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Puzzle.description'
        db.add_column(u'backend_puzzle', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Puzzle.name'
        db.add_column(u'backend_puzzle', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Puzzle.number'
        db.add_column(u'backend_puzzle', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TeamData.member1'
        db.delete_column(u'backend_teamdata', 'member1')

        # Deleting field 'TeamData.member2'
        db.delete_column(u'backend_teamdata', 'member2')

        # Deleting field 'TeamData.member3'
        db.delete_column(u'backend_teamdata', 'member3')

        # Deleting field 'TeamData.member4'
        db.delete_column(u'backend_teamdata', 'member4')

        # Deleting field 'TeamData.team_name'
        db.delete_column(u'backend_teamdata', 'team_name')

        # Deleting field 'Puzzle.description'
        db.delete_column(u'backend_puzzle', 'description')

        # Deleting field 'Puzzle.name'
        db.delete_column(u'backend_puzzle', 'name')

        # Deleting field 'Puzzle.number'
        db.delete_column(u'backend_puzzle', 'number')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'backend.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'answer': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hint1': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hint1_unlocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hint2': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hint2_unlocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hint3': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hint3_unlocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hint4': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hint4_unlocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hint5': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'hint5_unlocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle_unlocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'backend.teamdata': {
            'Meta': {'object_name': 'TeamData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'levels_solved': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'member1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'member2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'member3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'member4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'puzzle1_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle1_hintsused': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle1_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle1_started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle2_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle2_hintsused': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle2_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle2_started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle3_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle3_hintsused': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle3_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle3_started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle4_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle4_hintsused': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle4_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle4_started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle5_completed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'puzzle5_hintsused': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle5_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'puzzle5_started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['backend']