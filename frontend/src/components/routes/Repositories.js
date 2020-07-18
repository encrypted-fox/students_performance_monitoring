import React, {Component, Fragment} from 'react';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {deleteReposirory, getRepositories} from '../../actions/repositories';
import RepositoriesForm from '../forms/RepositoriesForm';
import RepositoriesFormEdit from '../forms/RepositoriesFormEdit';

class Repositories extends Component {
    static propTypes = {
        repositories: PropTypes.array.isRequired,
        getRepositories: PropTypes.func.isRequired,
        deleteReposirory: PropTypes.func.isRequired,
    };

    componentDidMount() {
        this.props.getRepositories();
    }

    render() {
        return (
            <Fragment>
                <h2 className='mb-3'>Реестр</h2>
                <table className='table table-striped table-borderless table-responsive'>
                    <thead className='thead-dark'>
                    <tr>
                        <th scope='col'>#</th>
                        <th scope='col'>Номер договора</th>
                        <th scope='col'>Инвентарный номер ФАП</th>
                        <th scope='col'>Имя создателя</th>
                        <th scope='col'>Email создателя</th>
                        <th scope='col'>Объем программы</th>
                        <th scope='col'>Тип системы</th>
                        <th scope='col'>Использовано</th>
                        <th scope='col'>Требования</th>
                        <th scope='col'>Описание</th>
                        <th scope='col'>Применение</th>
                        <th scope='col' className='text-left'>
                            Дата
                        </th>
                        <th/>
                        <th/>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.repositories.map((repository) => (
                        <tr key={repository.id}>
                            <td scope='row'>{repository.id}</td>
                            <td>{repository.agreement_id}</td>
                            <td>{repository.inventory_number}</td>
                            <td>{repository.name}</td>
                            <td>{repository.email}</td>
                            <td>{repository.volume}</td>
                            <td>{repository.os_type}</td>
                            <td>{repository.used_programs}</td>
                            <td>{repository.system_requirements}</td>
                            <td>{repository.program_description}</td>
                            <td>{repository.usage_description}</td>
                            <td>{repository.date}</td>
                            <td className=''>
                                <RepositoriesFormEdit data={repository}/>
                            </td>
                            <td className='text-right'>
                                <button
                                    onClick={this.props.deleteReposirory.bind(
                                        this,
                                        repository.id
                                    )}
                                    className='btn btn-danger btn-sm'>
                                    {' '}
                                    Удалить
                                </button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>

                <RepositoriesForm/>
            </Fragment>
        );
    }
}

const mapStateToProps = (state) => ({
    repositories: state.repositories.repositories,
});

export default connect(mapStateToProps, {getRepositories, deleteReposirory})(
    Repositories
);
