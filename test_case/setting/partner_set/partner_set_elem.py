# 股东
# 添加按钮 xpath pro环境
add_btn_elem = '//*[@id="body"]/setting/app-partner-set/div[1]/div[2]/button'
# 添加按钮 xpath dev环境
# add_btn_elem = '//*[@id="body"]/setting/app-partner-set/div[1]/div[2]/button'
# modal 框标题 class
modal_title_elem = '.modal-title'

# 添加股东
# 股东名称
partner_name_elem = '//*[@id="input-name"]'
# 实缴金额
actual_paid_elem = '//*[@id="submitAttempt"]/input'
# 保存按钮 xpath
save_btn_elem = '//*[@id="partnerDetailModal"]/div/div/div[3]/button[1]'
# 取消按钮 xpath
cancel_btn_elem = '//*[@id="partnerDetailModal"]/div/div/div[3]/button[2]'
# 关闭modal框按钮xpath
close_modal_btn_elem = '//*[@id="partnerDetailModal"]/div/div/div[1]/button/span'

# 股东列表
# 名称 id
table_tr_elem = 'departmentList'
table_partnerset_name_elem = 'departmentName'
table_actual_paid_elem = 'departmentType'

table_edit_btn_elem = '//*[@id="departmentList"]/td[3]'