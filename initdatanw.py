import pymysql
import csv
import pandas as pd


def init_mc_level_change_log_xxx():
    """
    2022-01-19
    处理em等级初始化数据
    :return:
    """
    path = '/Users/lhq/Downloads/lgm_init_uat_output_smalldata.sql'
    f = open(path, 'r')
    origin_datas = f.readlines()
    datas = list(map(lambda v: str(v).rstrip(';;\n').split('VALUES'), origin_datas))
    df = pd.DataFrame(datas, columns=['insert', 'values'])
    df_agg = df.groupby(by='insert', as_index=False).agg(list)
    df_agg['values'] = df_agg['values'].map(lambda v: ','.join(v))
    # print('\n')
    # info(df_agg.iloc[:3])
    # return
    df_agg['sql'] = df_agg.apply(lambda v: '{} values {};'.format(v['insert'], v['values']), axis=1)
    # x = df_agg['sql'].iloc[:3]
    df_agg['sql'].to_csv('/Users/lhq/Downloads/lgm_init_uat_output_smalldata_ok.csv', index=False)


def run_mc_level_change_log_xxx():
    fo = open('/Users/lhq/Downloads/lgm_init_uat_output_smalldata_ok.csv', 'r')
    csv_file = csv.reader(fo)
    for sql in csv_file:
        # print((",".join(sql)))
        sql = ",".join(sql)
        cursor.execute(sql)


if __name__ == '__main__':
    db = pymysql.connect(host="localhost", user="root", passwd="12345678", db="db")
    cursor = db.cursor()
    # init_mc_level_change_log_xxx()
    run_mc_level_change_log_xxx()
    cursor.close()
    db.commit()
    db.close()

