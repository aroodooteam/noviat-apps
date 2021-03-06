# -*- coding: utf-8 -*-
# Copyright 2009-2017 Noviat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def migrate(cr, version):

    module = 'account_bank_statement_advanced'
    view = 'absa_bank_statement_cancel_form_inherit'
    cr.execute(
        "SELECT res_id from ir_model_data "
        "WHERE module = %s "
        "AND name = %s",
        (module, view))
    res = cr.fetchone()
    if res:
        cr.execute(
            "DELETE from ir_ui_view WHERE id = %s" % res[0])

    cr.execute(
        "ALTER TABLE account_bank_statement "
        "DROP CONSTRAINT IF EXISTS account_bank_statement_name_uniq; "
        "DROP INDEX IF EXISTS account_bank_statement_name_non_slash_uniq; "
        "CREATE UNIQUE INDEX account_bank_statement_name_non_slash_uniq ON "
        "account_bank_statement(name, journal_id, fiscalyear_id, company_id) "
        "WHERE name !='/';")
