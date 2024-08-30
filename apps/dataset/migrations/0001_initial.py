# Generated by Django 4.1.10 on 2024-03-18 16:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataSet",
            fields=[
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="主键id",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="数据集名称")),
                ("desc", models.CharField(max_length=256, verbose_name="数据库描述")),
                (
                    "type",
                    models.CharField(
                        choices=[("0", "通用类型"), ("1", "web站点类型")],
                        default="0",
                        max_length=1,
                        verbose_name="类型",
                    ),
                ),
                ("meta", models.JSONField(default=dict, verbose_name="元数据")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="users.user",
                        verbose_name="所属用户",
                    ),
                ),
            ],
            options={
                "db_table": "dataset",
            },
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="主键id",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="文档名称")),
                (
                    "char_length",
                    models.IntegerField(verbose_name="文档字符数 冗余字段"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("0", "导入中"), ("1", "已完成"), ("2", "导入失败")],
                        default="0",
                        max_length=1,
                        verbose_name="状态",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("0", "通用类型"), ("1", "web站点类型")],
                        default="0",
                        max_length=1,
                        verbose_name="类型",
                    ),
                ),
                ("meta", models.JSONField(default=dict, verbose_name="元数据")),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.dataset",
                    ),
                ),
            ],
            options={
                "db_table": "document",
            },
        ),
        migrations.CreateModel(
            name="Paragraph",
            fields=[
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="主键id",
                    ),
                ),
                ("content", models.CharField(max_length=4096, verbose_name="段落内容")),
                (
                    "title",
                    models.CharField(default="", max_length=256, verbose_name="标题"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("0", "导入中"), ("1", "已完成"), ("2", "导入失败")],
                        default="0",
                        max_length=1,
                        verbose_name="状态",
                    ),
                ),
                ("hit_num", models.IntegerField(default=0, verbose_name="命中次数")),
                ("is_active", models.BooleanField(default=True)),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.dataset",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.document",
                    ),
                ),
            ],
            options={
                "db_table": "paragraph",
            },
        ),
        migrations.CreateModel(
            name="Problem",
            fields=[
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="主键id",
                    ),
                ),
                ("content", models.CharField(max_length=256, verbose_name="问题内容")),
                ("hit_num", models.IntegerField(default=0, verbose_name="命中次数")),
                (
                    "dataset",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.dataset",
                    ),
                ),
            ],
            options={
                "db_table": "problem",
            },
        ),
        migrations.CreateModel(
            name="ProblemParagraphMapping",
            fields=[
                (
                    "create_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="修改时间"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid1,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="主键id",
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.dataset",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.document",
                    ),
                ),
                (
                    "paragraph",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.paragraph",
                    ),
                ),
                (
                    "problem",
                    models.ForeignKey(
                        db_constraint=False,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dataset.problem",
                    ),
                ),
            ],
            options={
                "db_table": "problem_paragraph_mapping",
            },
        ),
    ]
